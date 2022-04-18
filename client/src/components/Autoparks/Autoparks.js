import React, {useEffect} from "react";
import {useDispatch, useSelector} from "react-redux";

import {getAllAutoParks} from "../../store/auto_park.slice";
import Autopark from "../Autopark/Autopark";

const Autoparks = () => {

    const {autoParks, status, error} = useSelector(state => state["autoParkReducer"]);

    const dispatch = useDispatch();

    useEffect(()=>{
        dispatch(getAllAutoParks())
        }, [])

    return (
        <div>
            {status === "pending" && <h2>Loading...</h2>}
            {error && <h2>{error}</h2>}
            {autoParks.map(autoPark => <Autopark key={autoPark.id} autoPark={autoPark}/>)}
        </div>
    );
};

export default Autoparks;