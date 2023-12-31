/* tslint:disable */
/* eslint-disable */
/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface CreateTaskRequest
 */
export interface CreateTaskRequest {
    /**
     * 
     * @type {string}
     * @memberof CreateTaskRequest
     */
    name: string;
}

/**
 * Check if a given object implements the CreateTaskRequest interface.
 */
export function instanceOfCreateTaskRequest(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "name" in value;

    return isInstance;
}

export function CreateTaskRequestFromJSON(json: any): CreateTaskRequest {
    return CreateTaskRequestFromJSONTyped(json, false);
}

export function CreateTaskRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): CreateTaskRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': json['name'],
    };
}

export function CreateTaskRequestToJSON(value?: CreateTaskRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
    };
}

