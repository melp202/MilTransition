import axios from 'axios';

import { GET_STATES } from './types';

// GET STATES
export const getStates = () => dispatch => {
	axios
		.get('/states/')
		.then(res => {
			dispatch({
				type: GET_STATES,
				payload: res.data
			});
		})
		.catch(err => console.log(err));
};
