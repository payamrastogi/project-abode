class Formatter:
    def get_formatted_info(self, processed_dict):
        message = ""
        if processed_dict:
            if 'address' in processed_dict:
                message += f"Address: {processed_dict['address']}\n"
            if 'homeType' in processed_dict:
                message += f"{processed_dict['homeType']} |"
            if 'price' in processed_dict:
                message += f" ${processed_dict['price']} |"
            if 'yearBuilt' in processed_dict:
                message += f" {processed_dict['yearBuilt']} |"
            if 'bedrooms' in processed_dict:
                message += f" {processed_dict['bedrooms']}B |"
            if 'bathrooms' in processed_dict:
                message += f" {processed_dict['bathrooms']}BA\n"
            if 'zestimate' in processed_dict:
                message += f" Z${processed_dict['zestimate']} |"
            if 'daysOnZillow' in processed_dict:
                message += f" {processed_dict['daysOnZillow']}D\n"
            if 'metropark' in processed_dict and 'duration' in processed_dict['metropark']:
                message += f"metropark: {processed_dict['metropark']['duration']} |"
        return message
