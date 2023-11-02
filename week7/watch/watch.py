import re

def parse(html):
    pattern = r'<iframe.*?src="(https?://(?:www\.)?youtube\.com/embed/(.*?))".*?>'
    match = re.search(pattern, html)
    if match:
        video_id = match.group(2)
        youtu_be_url = f"https://youtu.be/{video_id}"
        return youtu_be_url
    return None


def main():
    html = input("Enter HTML: ")
    youtube_url = parse(html)
    if youtube_url:
        print(youtube_url)
    else:
        print("None")

if __name__ == "__main__":
    main()