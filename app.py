"""Text-prompt interface for the original movie recommender."""
from recommender import recommend


def main():
    print('MOVIE MATCH | Content-based recommendations')
    print('Enter a description, such as: space science adventure')
    print('Type quit to exit.\n')
    while True:
        try:
            query = input('Your movie preferences: ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye!')
            break
        if query.lower() in {'quit', 'exit'}:
            print('Goodbye!')
            break
        try:
            results = recommend(query)
        except ValueError as exc:
            print(f'Please try again: {exc}\n')
            continue
        if not results:
            print('No matching movies. Try a genre or a broader keyword.\n')
            continue
        for index, (score, movie) in enumerate(results, 1):
            print(f"{index}. {movie['title']} ({movie['genres']}) | similarity {score:.3f}")
            print(f"   {movie['description']}")
        print()


if __name__ == '__main__':
    main()
