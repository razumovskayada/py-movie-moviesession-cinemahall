from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet | Movie:
    movies_queryset = Movie.objects.all()

    if not genres_ids and not actors_ids:
        return movies_queryset
    if genres_ids and actors_ids:
        movies_queryset = movies_queryset.filter(
            actors__id__in=actors_ids,
            genres__id__in=genres_ids
        )
    if genres_ids:
        movies_queryset = movies_queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies_queryset = movies_queryset.filter(actors__id__in=actors_ids)
    return movies_queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
