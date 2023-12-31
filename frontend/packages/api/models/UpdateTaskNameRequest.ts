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
 * @interface UpdateTaskNameRequest
 */
export interface UpdateTaskNameRequest {
    /**
     * 
     * @type {string}
     * @memberof UpdateTaskNameRequest
     */
    taskId: string;
    /**
     * 
     * @type {string}
     * @memberof UpdateTaskNameRequest
     */
    name: string;
}

/**
 * Check if a given object implements the UpdateTaskNameRequest interface.
 */
export function instanceOfUpdateTaskNameRequest(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "taskId" in value;
    isInstance = isInstance && "name" in value;

    return isInstance;
}

export function UpdateTaskNameRequestFromJSON(json: any): UpdateTaskNameRequest {
    return UpdateTaskNameRequestFromJSONTyped(json, false);
}

export function UpdateTaskNameRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): UpdateTaskNameRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'taskId': json['task_id'],
        'name': json['name'],
    };
}

export function UpdateTaskNameRequestToJSON(value?: UpdateTaskNameRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'task_id': value.taskId,
        'name': value.name,
    };
}

