import {Route, Routes} from "react-router-dom";

import CarsPage from "./pages/CarsPage/CarsPage";
import Layout from "./components/Layout/Layout";
import AutoparksPage from "./pages/AutoparksPage/AutoparksPage";

function App() {
    return (
        <div className="App">
            <Routes>
                <Route path="/" element={<Layout/>}>
                    <Route path="cars" element={<CarsPage/>}/>
                    <Route path="auto_parks" element={<AutoparksPage/>}/>
                    <Route path="auto_parks/:id" element={<CarsPage/>}/>
                </Route>
            </Routes>
        </div>
    );
}

export default App;
