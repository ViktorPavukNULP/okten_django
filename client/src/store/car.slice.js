import {createAsyncThunk, createSlice} from "@reduxjs/toolkit";

import {carService} from "../services/car.service";

export const getAllCars = createAsyncThunk(
    "carSlice/getAllCars",
    async (id, {rejectWithValue}) => {
        try {
            console.log(id)
            return await carService.getAll(id);
        } catch (e) {
            return rejectWithValue(e.message)
        }
    });


export const createCar = createAsyncThunk(
    "carSlice/createCar",
    async ({data}, {dispatch}) => {
        try {
            const newCar = await carService.create(data);
            dispatch(addCar({data: newCar}));
        } catch (e) {
            console.log(e);
        }
    });

export const deleteCar = createAsyncThunk(
    "carSlice/deleteCar",
    async ({id}, {dispatch}) => {
        try {
            await carService.deleteById(id);
            dispatch(removeCar({id}));
        } catch (e) {
            console.log(e);
        }
    });

export const updateCar = createAsyncThunk(
    "carSlice/updateCar",
    async ({id, newCar}, {dispatch}) => {
        try {
            await carService.update(id, newCar);
            dispatch(setCarForUpdate({id: '', brand: '', price: '', year: '', auto_park: ''}));
            dispatch(updateCarState({...newCar, id: id}));
        } catch (e) {
            console.log(e);
        }
    });

const carSlice = createSlice({
    name: "carSlice",
    initialState: {
        cars: [],
        carForUpdate: {id: '', brand: '', price: '', year: ''},
        status: null,
        error: null
    },
    reducers: {
        addCar: (state, action) => {
            state.cars.push(action.payload.data);
        },
        removeCar: (state, action) => {
            state.cars = state.cars.filter(car => car.id !== action.payload.id)
        },
        setCarForUpdate: (state, action) => {
            state.carForUpdate = action.payload;
        },
        updateCarState: (state, action) => {
            state.cars = state.cars.map(car => (car.id === action.payload.id ? action.payload : car));
        }
},
    extraReducers: {
        [getAllCars.pending]:
        (state) => {
            state.status = "pending";
        },
            [getAllCars.fulfilled]:
        (state, action) => {
            state.status = "fulfilled";
            state.cars = action.payload;
        },
            [getAllCars.rejected]:
        (state, action) => {
            state.status = "error";
            state.error = action.payload;
        }
    }
    })
    ;

const carReducer = carSlice.reducer;
export const {addCar, removeCar, setCarForUpdate, updateCarState} = carSlice.actions;
export default carReducer;
