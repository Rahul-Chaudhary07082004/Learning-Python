import json
yt = "youtube.txt"

def checking(videos):
    if not videos:
        print("No videos available.")
        return None
    
    while True:
            try:
                number = int(input("Enter the video number: "))

                if 1 <= number <= len(videos):
                    return number
                else:
                    print("Invalid index! Choose an existing video number.")

            except ValueError:
                print("Invalid input! Please enter a whole number.")

def load_data(): # display the data that is stored in list 
    try:
        with open(yt, 'r') as file:
            return json.load(file) # json.load -> load data from the file 
    except FileNotFoundError:
        return []

def save_videos_helper(videos): # it saves the data and keep list updated 
    with open(yt, 'w') as file:
        json.dump(videos, file) # json.dump -> basically store the file in videos

def list_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 50)

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_videos_helper(videos)
    print("Video added successfully!")

def update_videos(videos):
    list_videos(videos)
    # number = int(input("Enter the video number to update: "))
    index = checking(videos)
    # index = checking(videos)
    if index is None:
        return 
    name = input("Enter the new video name: ")
    time = input("Enter the new video time: ")
    videos[index-1] = {'name': name, 'time': time}
    save_videos_helper(videos)
    print("List has updated!")


def delete_videos(videos):
    list_videos(videos)
    # index = int(input("Enter the video number to be deleted: "))
    # if 1 <= index <= len(videos):
    index = checking(videos)
    if index is None:
        return
    
    del videos[index-1]
    save_videos_helper(videos)
    print("Video has deleted! ")


def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ") # give the list of yt videos
        print("2. Add a youtube video ") # add the yt video
        print("3. Update a youtube video details ") # update the yt video
        print("4. Delete a youtube video ") # delete the yt video
        print("5. Exit the app") # exit from app
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case "1":
                list_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()