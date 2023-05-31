import requests
import config_util


class GoogleClient:

    def __init__(self):
        self.api_key = config_util.read_google_api_key()

    def get_distance(self, origin, destination):
        new_dict = {}
        try:
            url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={self.api_key}"
            response = requests.get(url)
            data = response.json()
            print(data)
            # conversion factor
            conv_fac = 0.621371
            if data['status'] == 'OK':
                distance = data['rows'][0]['elements'][0]['distance']['value']
                miles = distance / 1000.0 * conv_fac
                new_dict['distance'] = f"{miles} miles"
                duration = data['rows'][0]['elements'][0]['duration']['text']
                new_dict['duration'] = f"{duration}"
        except Exception as e:
            print(e)
        return new_dict

    def get_travel_distance(self, origin):
        destinations = {
           "metropark": {
                   "address": "100 Middlesex Essex Turnpike, Iselin, NJ 08830"
           },
           "teb9": {
               "address": "601 Randolph Rd, Somerset, NJ 08873"
           },
           "jfk1": {
               "address": "1 John F Kennedy Blvd, Franklin Township, NJ 08873"
           }
        }
        for key in destinations.keys():
            new_dict = self.get_distance(origin, destinations[key]['address'])
            destinations[key].update(new_dict)
        return destinations


if __name__ == "__main__":
    google_client = GoogleClient()
    # Provide the origin and destination
    origin = "3 Prusakowski Blvd, Parlin, NJ 08859"
    # destination = "100 Middlesex Essex Turnpike, Iselin, NJ 08830"

    # Get the travel distance
    # distance = google_client.get_distance(origin, destination)
    # print(f"The estimated travel distance from {origin} to {destination} is {distance}.")

    lst = google_client.get_travel_distance(origin)
    print(lst)
