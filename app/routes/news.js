import Ember from 'ember';

export default Ember.Route.extend({
	redux: Ember.inject.service(),
  model() {
    var redux = this.get('redux');
    var startup = redux.getState().startups.current;
		var query = Ember.$.ajax({url: 'http://localhost:9000/api/news/' + startup, type: 'GET'})
			.then(function(response) {
				redux.dispatch({type: 'GET_NEWS', data: JSON.parse(response)})
			});
		return Ember.RSVP.hash({
			query: query,
		});
  }
});
