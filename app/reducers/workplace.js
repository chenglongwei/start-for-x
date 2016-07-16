const initialState = {
  all: [],
};

export default ((state, action) => {
  if (action.type === 'GET_WORKPLACE') {
    return Object.assign({}, state, {
      all: action.data
    });
  }
  
  return state || initialState;
});