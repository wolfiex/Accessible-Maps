import {
    writable,
    get
} from 'svelte/store';

export const datalayers = writable(); // which layers contain data e.g. ['centroids']


export const mapsource = writable({}); // source dictionary
export const maplayer = writable([]); // layer list
export const mapfunctions = writable([]);
export const mapobject = writable(undefined); // the mapbox 'map' object


// map constants

export let minzoom = 4;
export let maxzoom = 14;
export let drawtools = true


export const mapstyle ='./css/style-omt.json' 