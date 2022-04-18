import React from "react";
import {NavLink} from "react-router-dom";

import "./Header.css"

const Header = () => {
    return (
        <div className="Header">
            <NavLink to="/cars">All Cars</NavLink>
            <NavLink to="/auto_parks">Autoparks</NavLink>
        </div>
    );
};

export default Header;