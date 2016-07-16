import Ember from 'ember';

export default Ember.Route.extend({
	redux: Ember.inject.service(),
  model() {
    var redux = this.get('redux');
		var query = Ember.$.ajax({url: 'http://localhost:9000/api/finances/' + redux.getState().startups.current, type: 'GET'})
			.then(function(response) {
				redux.dispatch({type: 'GET_FINANCES', data: JSON.parse(response)})
			});
		return Ember.RSVP.hash({
			query: query,
		});
  }
});
