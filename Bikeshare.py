import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months =['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()
       if city in CITY_DATA:
           break

    # get user input for month (all, january, february, ... , june)
    month = input('All right! now it\'s time to provide us a month name ''or just say \'all\' to apply no month filter. \n(e.g. all, january, february, march, april, may, june)\n>'.format(months))
    while month != "all":
        if month in months:
                break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('One last thing. Could you type one of the week day you want to analyze?'' You can type \'all\' again to apply no day filter. \n(e.g. all, monday, sunday) \n> '.format(days))
    while day != "all":
        if day in days:
            break
      
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month =  months.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_month)

    # display the most common day of week
    most_day = df["day_of_week"].value_counts().idxmax()
    print("The most common day of week is :", most_day)

    # display the most common start hour
    most_hour = df["hour"].value_counts().idxmax()
    print("The most common start hour is :", most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df['Start Station'].value_counts().idxmax()
    print("The most start station is :", most_start_station)

    # display most commonly used end station
    most_end_station = df['End Station'].value_counts().idxmax()
    print("The most common End Station is :", most_end_station)

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if CITY_DATA == "washington":
        print ("no value")
    else:
        user_counts = df['User Type'].value_counts()
    print("Counts of user types:\n",user_counts )

    # Display counts of gender
    if 'Gender' in df.columns:
        print(user_stats_gender(df))
    else:
      print ("no value") 
    
def user_stats_gender(df):
    start_time = time.time()
    if CITY_DATA == "washington":
        print ("no value")
    else:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:\n",gender_counts)
    # Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    # the most common birth year
    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)
    # the most recent birth year
    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)
    # the most earliest birth year
    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break
            

def display_data(df):

    while True:
        response=['yes','no']
        choice= input("Would you like to view individual trip data (5 entries)? Type 'yes' or 'no'\n").lower()
        if choice in response:
            if choice=='yes':
                start=0
                end=5
                data = df.iloc[start:end,:9]
                print(data)
            break     
        else:
            print("Please enter a valid response")
    if  choice=='yes':       
            while True:
                choice_2= input("Would you like to view more trip data? Type 'yes' or 'no'\n").lower()
                if choice_2 in response:
                    if choice_2=='yes':
                        start+=5
                        end+=5
                        data = df.iloc[start:end,:9]
                        print(data)
                    else:    
                        break  
                else:
                    print("Please enter a valid response") 
           
def ask_more_data(df):
    more_data = input("Would you like to view 5 rows of data? Enter yes or no? ").lower()
    start_loc = 0
    while more_data == 'yes':
        print(df.iloc[0:5])
        start_loc += 5
        more_data = input("Would you like to view 5 rows of data? Enter yes or no? ").lower()
        
    return df 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        ask_more_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	    main()

