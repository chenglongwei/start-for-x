const initialState = {
  all: [],
};

export default ((state, action) => {
  if (action.type === 'GET_NEWS') {
    return Object.assign({}, state, {
      all: action.data
    });
  }

  return state || initialState;
});