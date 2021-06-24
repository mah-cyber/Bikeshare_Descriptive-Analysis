# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 01:19:26 2021

@author: Mahmoud
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Select city from the following (chicago, new york city, washington): ').lower()
            if city in ['chicago', 'new york city', 'washington']:
                break
        except ValueError :
            print('Error in typing.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('select month from the following (all, january, february, march, april, may, june): ').lower()
            if month in [ "all","january" , "february" , "march" ,"april", "may" ,"june"] :
                break
        except ValueError :
            print('Error in typing.')
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('select a week day: ').lower()
            if day in ["all","monday","tuseday","wednesday","thurday","friday","saturday","sunday"]:
                break
        except ValueError :
            print('Error in typing.')
            
                

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

   
    df['Start Time'] = pd.to_datetime(df['Start Time'])

  
    df['month'] = df['Start Time'].dt.month
     
    df['day'] = df['Start Time'].dt.day_name()
    
    df['hour'] = df['Start Time'].dt.hour
    
    
    
    if month != 'all':
       
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

      
        df = df[df['month'] == month]

   
    if day != 'all':
       
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()[0]
    print(' The most common month is {}.'.format(most_month))

    # TO DO: display the most common day of week
    most_day = df['day'].mode()[0]
    print('The most common day is {}.'.format(most_day))

    # TO DO: display the most common start hour
    most_hour = df['hour'].mode()[0]
    print('The most common start hour is {}.'.format(most_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start = df['Start Station'].mode()[0]
    print('The most common start station is {}.'.format(most_start))

    # TO DO: display most commonly used end station
    most_end = df['End Station'].mode()[0]
    print('The most common end station is {}.'.format(most_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['combined_station'] = df['Start Station'] + df['End Station']
    most_combination = df['combined_station'].mode()[0]
    print('The most frequent combination of start and end stations are {}.'.format(most_combination))
    
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time is: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types =  df["User Type"].value_counts()
    print('counts of user type are:', counts_of_user_types)
    # TO DO: Display counts of gender
    
    
    if 'Gender' in df:
        counts_of_gender =  df["Gender"].value_counts()
        print('counts of gender are:', counts_of_gender)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    
    
   
    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('earliest: ', earliest)
        print('most recent: ', most_recent)
        print('most common year: ', most_common_year)
    else:
         print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        start_loc = 0
    
        while view_data == 'yes':
            print(df.iloc[start_loc : start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
            
                                 
        
            
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
