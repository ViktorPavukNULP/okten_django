import {createAsyncThunk, createSlice} from "@reduxjs/toolkit";

import {autoParkService} from "../services/autoPark.service";

export const getAllAutoParks = createAsyncThunk(
    "autoParkSlice/getAllAutoParks",
    async (_, {rejectWithValue}) => {
        try {
            return await autoParkService.getAll();
        } catch (e) {
            return rejectWithValue(e.message)
        }
    });

const autoParkSlice = createSlice({
    name: "autoParkSlice",
    initialState: {
        autoParks: [],
        status: null,
        error: null
    },
    reducers: {
        addAutoPark: (state, action) => {
            state.autoParks.push(action.payload.data);
        },
        removeAutoPark: (state, action) => {
            state.autoParks = state.autoParks.filter(autoPark => autoPark.id !== action.payload.id)
        }
    },
    extraReducers: {
        [getAllAutoParks.pending]:
            (state) => {
                state.status = "pending";
            },
        [getAllAutoParks.fulfilled]:
            (state, action) => {
                state.status = "fulfilled";
                state.autoParks = action.payload;
            },
        [getAllAutoParks.rejected]:
            (state, action) => {
                state.status = "error";
                state.error = action.payload;
            }
    }
});

const autoParkReducer = autoParkSlice.reducer;
export const {addAutoPark, removeAutoPark,} = autoParkSlice.actions;
export default autoParkReducer;
