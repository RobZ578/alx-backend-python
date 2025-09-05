#!/usr/bin/python3
import seed


def stream_user_ages():
    """
    Generator that yields user ages one by one from the user_data table.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:  # only one loop
        yield row['age']
    cursor.close()
    connection.close()


def calculate_average_age():
    """
    Computes the average age using the stream_user_ages generator.
    """
    total_age = 0
    count = 0
    for age in stream_user_ages():  # second loop
        total_age += age
        count += 1

    average = total_age / count if count > 0 else 0
    print(f"Average age of users: {average}")


if __name__ == "__main__":
    calculate_average_age()
