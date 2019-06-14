import React, { Component } from 'react';
import ReactDom from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import { Link, Switch, Route } from 'react-router-dom';

// Import Components
import Header from './layout/Header';
import States from './transitioning/States';
import Stateform from './layout/Stateform';
import Organizations from './transitioning/Organizations';

// import store
import { Provider } from 'react-redux';
import store from '../store';

class App extends Component {
	render() {
		return (
			<Provider store={store}>
				<div>
					<nav className="navbar navbar-expand-sm navbar-dark bg-primary">
						<a className="navbar-brand" href="#">
							<Link to="/" style={{ textDecoration: 'none', color: '#fff' }}>
								MilTransition
							</Link>
						</a>
						<button
							className="navbar-toggler"
							type="button"
							data-toggle="collapse"
							data-target="#navbarColor01"
							aria-controls="navbarColor01"
							aria-expanded="false"
							aria-label="Toggle navigation"
						>
							<span className="navbar-toggler-icon" />
						</button>

						<div className="collapse navbar-collapse" id="navbarColor01">
							<ul className="navbar-nav mr-auto" />
						</div>
					</nav>
					{/* <Stateform /> */}
					<Switch>
						<Route exact path="/" component={States} />
						<Route path="/organization/" component={Organizations} />
					</Switch>
				</div>
			</Provider>
		);
	}
}

ReactDom.render(
	<Router>
		<App />
	</Router>,
	document.getElementById('app')
);
