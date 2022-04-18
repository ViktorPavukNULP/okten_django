import {axiosService} from "./axios.service";
import {urls} from "../constants/urls";


export const carService = {
    // getAll: () => axiosService.get(urls.cars).then(value => value.data),
    getAll: (id='') => axiosService.get(`${urls.cars}`).then(value => value.data.data),
    deleteById: (id) => axiosService.delete(`${urls.cars}${id}/`).then(value => value.data),
    create: (car) => axiosService.post(`${urls.cars}`,car).then(value => value.data),
    update: (id, newCar) => axiosService.patch(`${urls.cars}${id}/`,newCar)
}