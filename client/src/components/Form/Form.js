import React, {useEffect} from "react";
import {useForm} from "react-hook-form";
import {useDispatch, useSelector} from "react-redux";
import {joiResolver} from "@hookform/resolvers/joi";

import {createCar, updateCar} from "../../store/car.slice";
import {CarValidator} from "../../validators/car.validator";
import "./Form.css";

const Form = () => {
    const {handleSubmit, register, reset, setValue, formState: {errors}} = useForm({resolver: joiResolver(CarValidator), mode: "onTouched"});
    const dispatch = useDispatch();
    const {carForUpdate} = useSelector(state => state["carReducer"]);

    useEffect(() => {
        setValue("brand", carForUpdate.brand);
        setValue("price", carForUpdate.price);
        setValue("year", carForUpdate.year);
        setValue("auto_park", carForUpdate.auto_park);
    }, [carForUpdate])

    const submit = (data) => {
        dispatch(createCar({data}));
        reset();
    }
    const update = (data) => {
        dispatch(updateCar({id: carForUpdate.id, newCar: data}));
    }
    return (
        <form onSubmit={handleSubmit}>
            <div><label>Brand: <input type="text" {...register('brand')}/></label></div>
            {errors.brand && <div className="error">{errors.brand.message}</div>}
            <div><label>Price: <input type="text" {...register('price')}/></label></div>
            {errors.price && <div className="error">{errors.price.message}</div>}
            <div><label>Year: <input type="text" {...register('year')}/></label></div>
            {errors.year && <div className="error">{errors.year.message}</div>}
            <div><label>Autopark id: <input type="text" {...register('auto_park')}/></label></div>
            {errors.auto_park && <div className="error">{errors.auto_park.message}</div>}
            <div><button onClick={handleSubmit(submit)}>Create</button>
            {carForUpdate.id && <button onClick={handleSubmit(update)}>Update</button>}</div>
        </form>
    );
};

export default Form;