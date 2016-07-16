const initialState = {
  current: "start_for_x"
};

export default ((state, action) => {
  if (action.type === 'SET_CURRENT_STARTUP') {
    return Object.assign({}, state, {
      current: action.data
    });
  }

  return state || initialState;
});