from review_scrapper import ReviewScrapper


def main():
    try:
        ReviewScrapper(
            is_test=True,
        ).run()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
