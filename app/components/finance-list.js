import Ember from 'ember';
import hbs from 'htmlbars-inline-precompile';
import connect from 'ember-redux/components/connect';

function stateToComputed(state) {
  return {
    finances: state.finances.all
  };
};

function dispatchToActions(dispatch) {
  return {
  };
};

var FinanceListComponent = Ember.Component.extend({
	
});

export default connect(stateToComputed, dispatchToActions)(FinanceListComponent);