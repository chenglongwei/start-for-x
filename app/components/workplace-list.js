import Ember from 'ember';
import hbs from 'htmlbars-inline-precompile';
import connect from 'ember-redux/components/connect';

function stateToComputed(state) {
  return {
    workplace: state.workplace.all
  };
};

function dispatchToActions(dispatch) {
  return {
  };
};

var WorkplaceListComponent = Ember.Component.extend({

});

export default connect(stateToComputed, dispatchToActions)(WorkplaceListComponent);