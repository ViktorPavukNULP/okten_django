import Joi from "joi";

export const CarValidator = Joi.object({
    brand: Joi.string().regex(new RegExp('^[[A-Za-zА-яіїІЇёЁ]{1,20}$'))
        .messages({
            "string.pattern.base": "Only letters"
        }),
    price: Joi.number().min(0).max(1000000).required(),
    year: Joi.number().min(1990).max(new Date().getFullYear()).required(),
    auto_park: Joi.number().min(0).max(1000000)
});