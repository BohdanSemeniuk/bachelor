import React from "react";

const feature = {
    name: 'Movie1',
    description: 'Description about movie1',
    date: '24.02.2011',
    genres: ['history', 'action'],
    directors: ['Lebron', 'Mason'],
    actors: ['Smith', 'Diesel', 'Virtus'],
    budget: '176_500_000',
    fees_in_world: '435_000_000',
}

export default function MovieDetail() {
    return (
        <div className="overflow-hidden bg-white py-24 sm:py-32">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div className="text-center">
                    <img
                        src="https://tailwindui.com/img/component-images/dark-project-app-screenshot.png"
                        alt="Product screenshot"
                        className="rounded-lg shadow-lg"
                        height="550vh"
                    />
                </div>
                <div className="px-0.5 mx-2">
                    <h1 className="text-4xl font-bold mb-4">{feature.name}</h1>
                    <p className="text-gray-700 text-lg mb-4">{feature.description}</p>
                    <hr className="my-4" />
                    <p>
                        <span className="text-gray-500 font-bold">Дата виходу: </span>
                        {feature.date}
                    </p>
                    <p>
                        <span className="text-gray-500 font-bold">Жанр: </span>
                        {feature.genres.map((genre) => genre).join(", ")}
                    </p>
                    <p>
                        <span className="text-gray-500 font-bold">Режисери: </span>
                        {feature.directors.map((director) => director).join(", ")}
                    </p>
                    <p>
                        <span className="text-gray-500 font-bold">Актори: </span>
                        {/*{feature.actors.map((actor) => actor.name).join(", ")}*/}
                        {feature.actors.map((actor) => actor).join(", ")}
                    </p>
                    <p>
                        <span className="text-gray-500 font-bold">Бюджет: </span>
                        {feature.budget}
                    </p>
                    <p>
                        <span className="text-gray-500 font-bold">Касові збори: </span>
                        {feature.fees_in_world}
                    </p>
                    <hr className="my-4" />
                </div>
            </div>
            <div className="text-center responsive-iframe-container">
                <iframe
                    width="860"
                    height="480"
                    src={`https://www.youtube.com/embed/535435`}
                    // src={`https://www.youtube.com/embed/${movie.youtube_trailer_url}`}
                    title="YouTube video player"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                    className="responsive-iframe"
                />
            </div>
        </div>
    )
}