"""Download all Strava data from a user"""
from .utils import polyline_to_latlong
import pandas as pd
def get_user_data(authenticated_client, user_name, output_prefix):
    """
    Get all activities of Strava user and save to a csv.

    Args:
        authenticated_client (Strava_Client): OAuth authenticated instance of Strava_Client.
        user_name (string): Unique username to add to saved csv.
        output_prefix (string): Path to folder where to save resulting csv containing segments.

    Returns:
        list: List of activities (dictionaries).
    """
    print('Collecting user data \nPage:')
    activites_url = "https://www.strava.com/api/v3/athlete/activities"
    page = 1
    activities = []
    while True:
        param = {'per_page': 200, 'page': page}
        response = authenticated_client.get(activites_url, params=param).json()
        if len(response) == 0:
            break
        activities += response
        print(f'{str(page)}')
        page += 1
    
    activities = prepare_activities(activities)

    filename = output_prefix + user_name + '.csv'
    pd.DataFrame(activities).to_csv(filename, index=False)

    return activities

def prepare_activities(activities):
    """
    Pre-process activities.
    
    Convert Google Polylines to latlong lists.

    Args:
        activities (list): List of activities (dictionaries).

    Returns:
        activities (list): List of activities (dictionaries).
    """
    for activity_i, _ in enumerate(activities):
        activities[activity_i]['map']['summary_polyline'] = polyline_to_latlong(activities[activity_i]['map']['summary_polyline'])

    return activities


