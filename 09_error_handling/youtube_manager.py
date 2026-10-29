import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def list_videos(videos):
    pass

def add_videos(videos):
    pass

def update_videos(videos):
    pass

def delete_videos(videos):
    pass

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ") # give the list of yt videos
        print("2. Add a youtube video ") # add the yt video
        print("3. Update a youtube video details ") # update the yt video
        print("4. Delete a youtube video ") # delete the yt video
        print("5. Exit the app") # exit from app
        choice = input("Enter your choice")

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