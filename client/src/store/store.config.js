import {configureStore} from "@reduxjs/toolkit";

import carReducer from "./car.slice";
import autoParkReducer from "./auto_park.slice";

const store = configureStore({
    reducer: {
        carReducer,
        autoParkReducer
    }
});

export default store;
