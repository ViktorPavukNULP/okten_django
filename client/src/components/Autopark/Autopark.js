import React from "react";

import {Link} from "react-router-dom";

import "./Autopark.css";

const Autopark = ({autoPark}) => {

    return (

        <div className="AutoPark">
            <Link to={`/auto_parks/${autoPark.id}`}>
                {autoPark.id}. {autoPark.name}
            </Link>
        </div>
    );
};

export default Autopark;