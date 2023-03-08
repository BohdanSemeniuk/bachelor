import React from "react";
import HeroSection from "./components/HeroSection";
import { Route, Routes} from "react-router-dom";
import MovieList from "./components/MovieList";
import MovieDetail from "./components/MovieDetail";

function App() {
    return (
        <>
            <Routes>
                <Route path="/" element={<HeroSection />}/>
                <Route path="/movie_list" element={<MovieList />}/>
                <Route path=":name" element={<MovieDetail />}/>
            </Routes>
        </>
    );
}

export default App;