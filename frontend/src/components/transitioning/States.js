import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getStates } from '../../actions/states';
import { Link, Switch, Route } from 'react-router-dom';

class States extends Component {
	static propTypes = {
		states: PropTypes.array.isRequired
	};

	componentDidMount() {
		this.props.getStates();
	}

	render() {
		return (
			<div className="container" style={{ textAlign: 'center' }}>
				{this.props.states.map(state => (
					<Link to="/organization/">
						<div className="card mb-3" key={state.id}>
							<h3 className="card-header">{state.name}</h3>
							<img
								style={{ height: '200px', width: '100%', display: 'block' }}
								src={state.state_flag}
								alt="Card image"
							/>
							<div className="card-body">
								<a href="#" className="card-link">
									View Organizations
								</a>
							</div>
						</div>
					</Link>
				))}
			</div>
		);
	}
}

const mapStateToProps = state => ({
	states: state.statesReducer.states
});

export default connect(
	mapStateToProps,
	{ getStates }
)(States);
