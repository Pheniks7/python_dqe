from task_5_classes import NewsFeed

if __name__ == "__main__":
    # task_5 = NewsFeed()
    # task_5.add_content_manually()
    # task_5.add_content_manually()
    # task_5.add_content_manually()
    # task_5.show_news_feed()
    # task_5.save_as_file()
    task_6 = NewsFeed()
    check_point = task_6.read_file()
    if check_point is not None:
        task_6.save_as_file()
