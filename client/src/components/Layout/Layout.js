import React from "react";
import {Outlet} from "react-router-dom";

import Header from "../Header/Header";
import "./Layout.css";

const Layout = () => {
    return (
        <div className="Layout">
            <Header/>
            <div className="Outlet"><Outlet/></div>
        </div>
    );
};

export default Layout;