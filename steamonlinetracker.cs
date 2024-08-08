using System;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

class steamonlinetracker
{
    static async Task Main(string[] args)
    {
        // Input API key and Steam ID
        Console.Write("Enter your Steam API key: ");
        string apiKey = Console.ReadLine().Trim();

        Console.Write("Enter the Steam ID of the user: ");
        string steamId = Console.ReadLine().Trim();

        int? onlineStatus = null;

        while (true)
        {
            var userInfo = await GetUserInfo(apiKey, steamId);

            if (userInfo != null)
            {
                int currentStatus = userInfo.Value.personastate;
                string personaname = userInfo.Value.personaname;
                string profileurl = userInfo.Value.profileurl;
                string avatar = userInfo.Value.avatar;
                long lastlogoff = userInfo.Value.lastlogoff;
                long timecreated = userInfo.Value.timecreated;

                string lastlogoffStr = lastlogoff > 0 ? DateTimeOffset.FromUnixTimeSeconds(lastlogoff).ToString("yyyy-MM-dd HH:mm:ss") : "N/A";
                string timecreatedStr = timecreated > 0 ? DateTimeOffset.FromUnixTimeSeconds(timecreated).ToString("yyyy-MM-dd HH:mm:ss") : "N/A";

                Console.WriteLine($"User: {personaname}");
                Console.WriteLine($"Profile URL: {profileurl}");
                Console.WriteLine($"Avatar URL: {avatar}");
                Console.WriteLine($"Last Logoff: {lastlogoffStr}");
                Console.WriteLine($"Account Created: {timecreatedStr}");

                // Check if the status has changed to "online"
                if (currentStatus == 1 && onlineStatus != 1)
                {
                    onlineStatus = currentStatus;
                    Console.WriteLine($"The user came online at {DateTime.Now:yyyy-MM-dd HH:mm:ss}");
                }
            }

            await Task.Delay(60000); // Check the status every 60 seconds
        }
    }

    static async Task<(int personastate, string personaname, string profileurl, string avatar, long lastlogoff, long timecreated)?> GetUserInfo(string apiKey, string steamId)
    {
        string url = $"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={apiKey}&steamids={steamId}";

        try
        {
            using HttpClient client = new HttpClient();
            HttpResponseMessage response = await client.GetAsync(url);
            response.EnsureSuccessStatusCode();

            string responseBody = await response.Content.ReadAsStringAsync();
            JObject data = JObject.Parse(responseBody);

            // Retrieve user information
            var players = data["response"]?["players"];
            if (players != null && players.HasValues)
            {
                var player = players.First;

                return (
                    personastate: player.Value<int?>("personastate") ?? 0,
                    personaname: player.Value<string>("personaname"),
                    profileurl: player.Value<string>("profileurl"),
                    avatar: player.Value<string>("avatar"),
                    lastlogoff: player.Value<long?>("lastlogoff") ?? 0,
                    timecreated: player.Value<long?>("timecreated") ?? 0
                );
            }
            else
            {
                Console.WriteLine("Error retrieving user data.");
                return null;
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"An error occurred: {e.Message}");
            return null;
        }
    }
}