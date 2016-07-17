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
	didInsertElement() { 
		Ember.$(function () {
			    Ember.$('#container').highcharts({
			        title: {
			            text: 'Amount Raised',
			            x: -20 //center
			        },
			        xAxis: {
			            categories: ["Seed", "Series A", "Series B", "Series C"]
			        },
			        yAxis: {
			            title: {
			                text: 'Funding'
			            },
			            plotLines: [{
			                value: 0,
			                width: 1,
			                color: '#808080'
			            }]
			        },
			        tooltip: {
			            valueSuffix: '°C'
			        },
			        legend: {
			            layout: 'vertical',
			            align: 'right',
			            verticalAlign: 'middle',
			            borderWidth: 0
			        },
			        series: [{
			            name: 'Amia',
			            data: [20000, 900000, 1300000]
			        }, {
			            name: 'WikiBrains',
			            data: [750000]
			        }, {
			            name: 'OneClass',
			            data: [635000, 1600000]
			        }, {
			            name: 'ClassKick',
			            data: [60000, 1200000]
			        }]
			    });
			});
	}
	
});

export default connect(stateToComputed, dispatchToActions)(FinanceListComponent);