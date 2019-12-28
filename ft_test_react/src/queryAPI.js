import axios from 'axios'
import MockAdapter from 'axios-mock-adapter'

let mock = new MockAdapter(axios);

export const queryAPI = () => {
    return axios.get('/get-data');
}
 

mock.onGet('/get-data').reply(200, {
    data: "A0B3HCJ"
});
