import time
from datetime import datetime, timezone, timedelta

from sqlalchemy import func

# print (time.time())
# print (time.gmtime())
# print (time.localtime())
# print (datetime.now(timezone.utc))
# print (time.time_ns()) # integer nanoseconds since the epoch

# 1688645100000000000 is 2023 July 6 12:05pm GMT

            # # Assuming you have a SQLAlchemy model named 'YourModel' with a column named 'timestamp' representing the nanoseconds since the epoch

            # # Retrieve the nanoseconds from the database
            # # nanoseconds = db.session.query(YourModel.timestamp).scalar()

            # nanoseconds = 1688645100000000000

            # # Convert nanoseconds to a datetime object
            # seconds = nanoseconds // 1_000_000_000
            # subseconds = (nanoseconds % 1_000_000_000) / 1_000_000.0
            # timestamp = datetime.datetime.utcfromtimestamp(seconds) + datetime.timedelta(milliseconds=subseconds)

            # # Format the timestamp in a human-readable way
            # formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")

            # # Output the formatted timestamp
            # print(formatted_timestamp)


# import datetime
# import time

# # Get the current time in nanoseconds
# current_time_ns = time.time_ns()

# # Convert nanoseconds to a datetime object
# current_time = datetime.datetime.fromtimestamp(current_time_ns / 1e9)

# # Format the datetime object as a human-readable string
# formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# # Output the formatted time
# print(formatted_time)

# # Parse the date and time string into a datetime object
# date_time = datetime.datetime.strptime(formatted_time, "%Y-%m-%d %H:%M:%S")

# # Convert the datetime object to the number of seconds since the epoch
# epoch_seconds = (date_time - datetime.datetime(1970, 1, 1)).total_seconds()

# # Output the epoch seconds
# print(int(epoch_seconds))



import datetime
import time

print ('the local time now is')
print(datetime.datetime.fromtimestamp(time.time_ns() / 1e9).strftime("%Y-%m-%d %H:%M:%S"))


print(datetime.datetime.fromtimestamp(1688688049).strftime("%Y-%m-%d %H:%M:%S"))



# Get the current time in nanoseconds
current_time_ns = time.time_ns()

# Convert nanoseconds to a datetime object in UTC
current_time = datetime.datetime.fromtimestamp(current_time_ns / 1e9)

# Format the datetime object as a human-readable string
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Output the formatted time
print(formatted_time) # in UTC time

import datetime

# Define the local time string in "%Y-%m-%d %H:%M:%S" format
local_time_string = formatted_time

# Convert the local time string to a datetime object
local_time = datetime.datetime.strptime(local_time_string, "%Y-%m-%d %H:%M:%S")

# Calculate the epoch time in seconds for the local time
epoch_seconds = int((local_time - datetime.datetime(1970, 1, 1)).total_seconds())

# Convert the epoch seconds to nanoseconds
nanoseconds = int(epoch_seconds * 1e9)

# Output the nanoseconds
print('seconds since epoch')
print(epoch_seconds)
print('nanoseconds since epoch')
print(nanoseconds)