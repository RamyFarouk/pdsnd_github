import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago','new york city','washington']
months = ['january', 'february', 'march', 'april', 'may', 'june']
days=['monday', 'tuesday','wednesday','thursday','friday','saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington)

    city = input("select a city to explore (chicago, new york city or washington):").lower()
    while city not in cities:
        print('sorry you enterd invalid city to explore')
        city=input('please reselect a city from these available cities(chicago, new york city or washington):').lower()
    print("you select {}".format(city))
    print('-'*40)

    # get user input for a month (all,january,february,...june)

    month=input('Now enter a month to explore from (january,february,...june) or enter all to explore all months ').lower()
    while (month != 'all') and (month not in months):
        print("sorry an invalid month was enetered and available months are from january to june")
        month = input('please enter an available month to explore:').lower()
    print("you select {}".format(month))
    print('-'*40)

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day =input("select a day of week to search for (monday, tuesday, ... sunday) or select all:").lower()
    while (day != 'all') and (day not in days):
        print("sorry you entered a wrong day format \n")
        day = input('please enter a vaild day format from (monday,tuesday,wendesday,thursday,friday,saturday,sunday):').lower()
    print("you select {}".format(day))
    print('-' * 40)
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
    df=pd.read_csv(CITY_DATA[city])
    # convert Satrt Time to datetime format:
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # select month from date:
    df['month'] = df['Start Time'].dt.month
    # select day from date:
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # select starting travel hour:
    df['Travel_hour']=df['Start Time'].dt.hour
    # filter by selected month:
    if month != 'all':
        month = months.index(month)-1
        df = df[df['month'] == month]
    # filter by selected day:
    if day != 'all':
        df= df[df['day_of_week'] == day.title()]
    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most travel  month
    if month=='all':
        common_travel_month = df['month'].mode()[0]
        common_month_name = months[common_travel_month-1]
        print('The most common month is {}\n'.format(common_month_name))
    else:
        print("You have selected to see only the rides that happened in {}.\n".format(month))



    # display the most common day of week
    if day=='all':
        common_travel_day=df['day_of_week'].mode()[0]
        print('The most common travel day is {}\n'.format(common_travel_day))
    else:
        print("You have selected to see only the rides that happened in {}.\n".format(day))


    # display the most common travel start hour
    common_starting_travel_hour=df['Travel_hour'].mode()[0]
    print('The most common starting travel hour is {}\n'.format(common_starting_travel_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {}".format(most_common_start_station))

    # display most commonly used end station

    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is {}'.format(most_common_end_station))

    # display most frequent combination of start station and end station trip

    df['Start-End Combination'] = df['Start Station'] + ' - ' + df['End Station']
    most_common_start_end_combination = df['Start-End Combination'].mode()[0]
    print('The most common start-end combination is {}'.format(most_common_start_end_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = (str(int(total_travel_time//86400)) +'d ' +
                         str(int((total_travel_time % 86400)//3600)) +'h '+
                         str(int(((total_travel_time % 86400) % 3600)//60)) +'m '+
                         str(int(((total_travel_time % 86400) % 3600) % 60)) + 's')

    print('the total travel time is : {}\n'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' +
                        str(int(mean_travel_time % 60)) + 's')

    print('The mean travel time is {}\n'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

     # Display counts of user types
    customers = df.groupby('User Type')['User Type'].count().to_string(header = False)
    print("The count of each type of user is\n {}\n".format(customers))
    # Display counts of gender
    if "Gender" in df.columns:
        gender = df.groupby('Gender')['Gender'].count().to_string(header = False)
        print("The count of the users by gender is\n {}".format(gender))
    else:
        print("The data from this city did not include gender\n")
    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        oldest_customer = df['Birth Year'].min()
        print("The oldest customer was born in:", int(oldest_customer), '\n')
        youngest_customer = df['Birth Year'].max()
        print("The youngest customer was born in: ", int(youngest_customer), "\n")
        most_common_date_of_birth = df['Birth Year'].mode()
        print("The most common customers were born in: ", int(most_common_date_of_birth), "\n")
    else:
        print("The data from this city did not include date of birth.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, start):
    '''Raw data is displayed upon request by the user as follows:
    Script should ask the users if they want to see 5 lines of raw data,
    display that data if the answer is 'yes', and continue asking to display
    another 5 lines until the user says 'no
    '''
    raw_data = input("Would you like to view individual trip data?\n"
                "yes or no: ")
    raw_data = raw_data.lower()
    while True:
        if raw_data == 'yes':
            print(df.iloc[start:start+5])
            start += 5
            return display_data(df, start)
        elif raw_data == 'no':
            return
        else:
            print("If you do not want to display data Just say no .")
            return display_data(df, start)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df, 0)

        restart = input("Would you like to restart? yes or no: ")
        answer=['yes','no']
        while restart.lower() not in answer:
            print("Invalid input. Please type 'yes' or 'no'.")
            restart = input("Would you like to restart? yes or no: ")
        if restart.lower() == 'yes':
            main()
        elif restart.lower() == 'no':
            break

if __name__ == "__main__":
    main()
