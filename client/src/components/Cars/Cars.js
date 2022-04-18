import React, {useEffect} from "react";
import {useDispatch, useSelector} from "react-redux";

import Car from "../Car/Car";
import {getAllCars} from "../../store/car.slice";
import {useParams} from "react-router-dom";

const Cars = () => {
    const {cars, status, error} = useSelector(state => state["carReducer"]);
    const dispatch = useDispatch();

    const {id} = useParams();

    useEffect(() => {
        dispatch(getAllCars(id));
    }, [id]);

    return (
        <div>
            {status === "pending" && <h2>Loading...</h2>}
            {error && <h2>{error}</h2>}
            {cars.map(car => <Car key={car.id} car={car}/>)}
        </div>
    );
};

export default Cars;