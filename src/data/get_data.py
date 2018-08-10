import os
import json
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests

# Note, I saw nothing restricting this script from scraping when I looked at robots.txt

states = {'ALABAMA': 'AL', 'ALASKA': 'AK', 'ARIZONA': 'AZ', 'ARKANSAS': 'AR', 'CALIFORNIA': 'CA', 'COLORADO': 'CO',
          'CONNECTICUT': 'CT', 'DELAWARE': 'DE', 'FLORIDA': 'FL', 'GEORGIA': 'GA', 'HAWAII': 'HI', 'IDAHO': 'ID',
          'ILLINOIS': 'IL', 'INDIANA': 'IN', 'IOWA': 'IA', 'KANSAS': 'KS', 'KENTUCKY': 'KY', 'LOUISIANA': 'LA',
          'MAINE': 'ME', 'MARYLAND': 'MD', 'MASSACHUSETTS': 'MA', 'MICHIGAN': 'MI', 'MINNESOTA': 'MN',
          'MISSISSIPPI': 'MS', 'MISSOURI': 'MO', 'MONTANA': 'MT', 'NEBRASKA': 'NE', 'NEVADA': 'NV',
          'NEW HAMPSHIRE': 'NH', 'NEW JERSEY': 'NJ', 'NEW MEXICO': 'NM', 'NEW YORK': 'NY', 'NORTH CAROLINA': 'NC',
          'NORTH DAKOTA': 'ND', 'OHIO': 'OH', 'OKLAHOMA': 'OK', 'OREGON': 'OR', 'PENNSYLVANIA': 'PA',
          'RHODE ISLAND': 'RI', 'SOUTH CAROLINA': 'SC', 'SOUTH DAKOTA': 'SD', 'TENNESSEE': 'TN', 'TEXAS': 'TX',
          'UTAH': 'UT', 'VERMONT': 'VT', 'VIRGINIA': 'VA', 'WASHINGTON': 'WA', 'WEST VIRGINIA': 'WV', 'WISCONSIN': 'WI',
          'WYOMING': 'WY', 'GUAM': 'GU', 'PUERTO RICO': 'PR', 'VIRGIN ISLANDS': 'VI'}

url_base = 'http://www.tweetcongress.org/api/tweeters/state/'


def get_cman_info(state):
    """
    Will take a list of congressmen and return the relevant attributes
    :param congress_list: list of divs that contain congress data
    :param state: state you are scraping
    :return: list of relevant scraped attributes
    """

    cman_attrs = []
    abbrev = states[state]
    r = requests.get(url_base + abbrev)
    d = json.loads(r.text)

    for cman in d['tweeters']:
        _id = cman.get('_id', '')
        dateOfBirth = cman.get('dateOfBirth', '')
        email = cman.get('email', '')
        facebookUserName = cman.get('facebookUserName', '')
        fullName = cman.get('fullName', '')
        gender = cman.get('gender', '')
        address = cman['office'].get('address', '')
        chamber = cman['office'].get('chamber', '')
        country = cman['office'].get('country', '')
        district = cman['office'].get('district', '')
        leadershipRole = cman['office'].get('leadershipRole', '')
        party = cman['office'].get('party', '')
        state = cman['office'].get('state', '')
        termEnd = cman['office'].get('termEnd', '')
        termStart = cman['office'].get('termStart', '')
        title = cman['office'].get('title', '')
        phone = cman.get('phone', '')
        profileImageSmall = cman.get('profileImageSmall', '')
        slug = cman.get('slug', '')
        followersCount = cman['twitterProfile'].get('followersCount', '')
        friendsCount = cman['twitterProfile'].get('friendsCount', '')
        idStr = cman['twitterProfile'].get('idStr', '')
        name = cman['twitterProfile'].get('name', '')
        profileImageUrl = cman['twitterProfile'].get('profileImageUrl', '')
        screenName = cman['twitterProfile'].get('screenName', '')
        statusesCount = cman['twitterProfile'].get('statusesCount', '')
        url = cman['twitterProfile'].get('url', '')
        verified = cman['twitterProfile'].get('verified', '')
        twitterUserName = cman.get('twitterUserName', '')
        website = cman.get('website', '')

        cman_attrs.append(
            [_id, dateOfBirth, email, facebookUserName, fullName, gender, address, chamber, country, district,
             leadershipRole, party, state, termEnd, termStart, title, phone, profileImageSmall, slug, followersCount,
             friendsCount, idStr, name, profileImageUrl, screenName, statusesCount, url, verified, twitterUserName,
             website])
    return cman_attrs


if __name__ == '__main__':
    """
    Scrapes tweetcongress.org for congressman information especially twitter info
    """

    congress_info = []

    for state in states.keys():
        congress_info.append(get_cman_info(state))
    congress_info_flatter = [cman for state_congress in congress_info for cman in state_congress]
    columns = ['_id', 'dateOfBirth', 'email', 'facebookUserName', 'fullName', 'gender', 'address', 'chamber', 'country', 'district',
               'leadershipRole', 'party', 'state', 'termEnd', 'termStart', 'title', 'phone', 'profileImageSmall', 'slug', 'followersCount',
               'friendsCount', 'idStr', 'name', 'profileImageUrl', 'screenName', 'statusesCount', 'url', 'verified', 'twitterUserName',
               'website']
    df = pd.DataFrame(congress_info_flatter, columns=columns)

    proj_dir = Path(__file__).parents[2]
    filename = proj_dir/"data"/"raw"/"congressmen_data.csv"
    print(filename)

    us_state_abbrev = {
        'AL': 'Alabama',
        'AK': 'Alaska',
        'AZ': 'Arizona',
        'AR': 'Arkansas',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'IA': 'Iowa',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'ME': 'Maine',
        'MD': 'Maryland',
        'MA': 'Massachusetts',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MS': 'Mississippi',
        'MO': 'Missouri',
        'MT': 'Montana',
        'NE': 'Nebraska',
        'NV': 'Nevada',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NY': 'New York',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VT': 'Vermont',
        'VA': 'Virginia',
        'WA': 'Washington',
        'WV': 'West Virginia',
        'WI': 'Wisconsin',
        'WY': 'Wyoming',
    }
    df = pd.read_csv(proj_dir/"data"/"raw"/"congressmen_data.csv")
    df = df.drop(df.columns[0], axis=1)
    df.dateOfBirth = pd.to_datetime(df.dateOfBirth)
    df.termEnd = pd.to_datetime(df.termEnd)
    df.termStart = pd.to_datetime(df.termStart)
    df.party = df.party.astype("category")
    df.chamber = df.chamber.astype("category")
    df.gender = df.gender.astype("category")
    df.state = df.replace({"state": us_state_abbrev}).state
    df.state = df.state.astype("category")

    df.to_csv(filename)
    df.to_feather(filename.stem/'.feather')

