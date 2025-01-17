import React from 'react';
import { connect } from 'react-redux';
import { reduxForm, formValueSelector } from 'redux-form';
import {
  Modal, Button, Form, Row, Col, ButtonToolbar
} from 'react-bootstrap';
import { DraggableModal } from '../DraggableModal';
import validate from './validate';
import warn from './warning';
import JSForm from '@rjsf/core';
import classNames from 'classnames';
import './style.css';

import {
  FieldsHeader,
  StaticField,
  InputField,
} from './fields';

import { SPACE_GROUPS } from '../../constants';

class GenericTaskForm extends React.Component {
  constructor(props) {
    super(props);

    this.submitAddToQueue = this.submitAddToQueue.bind(this);
    this.showFooter = this.showFooter.bind(this);
    this.showDCFooter = this.showDCFooter.bind(this);
    this.showDPFooter = this.showDPFooter.bind(this);
    this.submitRunNow = this.submitRunNow.bind(this);
    this.addToQueue = this.addToQueue.bind(this);
    this.resetParameters = this.resetParameters.bind(this);
    this.defaultParameters = this.defaultParameters.bind(this);
    this.jsformData = {};
  }

  submitAddToQueue() {
    this.props.handleSubmit(this.addToQueue.bind(this, false))();
  }

  submitRunNow() {
    this.props.handleSubmit(this.addToQueue.bind(this, true))();
  }

  addToQueue(runNow, params) {
    const parameters = {
      ...params,
      ...this.jsformData,
      label: params.name,
      shape: this.props.pointID,
      selection: this.props.taskData.parameters.selection
    };

    // Form gives us all parameter values in strings so we need to transform numbers back
    const stringFields = [
      'shutterless',
      'inverse_beam',
      'centringMethod',
      'detector_mode',
      'space_group',
      'prefix',
      'subdir',
      'type',
      'shape',
      'label',
      'helical',
      'selection'
    ];

    this.props.addTask(parameters, stringFields, runNow);
    this.props.hide();
  }

  resetParameters(form) {
    this.props.reset(form.toLowerCase());
  }

  defaultParameters() {
    const { type } = this.props.taskData;
    this.props.resetTaskParameters();
    this.resetParameters(type);
    const fieldNames = Object.keys(this.props.initialParameters[type.toLowerCase()]);
    fieldNames.forEach((field) => {
      this.props.autofill(type.toLowerCase(), field, this.props.initialParameters[type.toLowerCase()][field]);
    });
  }


  showDCFooter() {
    return (
      <Modal.Footer>
        <div className="input-group-btn d-flex">
          <ButtonToolbar style={{ bottom: '15px', left: '10px' }} className="position-absolute">
            <Button
              size="sm"
              variant="outline-secondary"
              onClick={this.defaultParameters}
            >
              Default Parameters
            </Button>
          </ButtonToolbar>
          <ButtonToolbar>
            <Button
              className='me-3 ms-3'
              size="sm"
              variant="success"
              disabled={this.props.taskData.parameters.shape === -1 || this.props.invalid}
              onClick={this.submitRunNow}
            >
              Run Now
            </Button>
            <Button
              size="sm"
              variant="outline-secondary"
              disabled={this.props.invalid}
              onClick={this.submitAddToQueue}
            >
              {this.props.taskData.sampleID ? 'Change' : 'Add to Queue'}
            </Button>
          </ButtonToolbar>
        </div>
      </Modal.Footer>
    );
  }

  showDPFooter() {
    return (
      <Modal.Footer>
        <ButtonToolbar className="pull-right">
          <Button
            className='me-3'
            variant="success"
            disabled={this.props.taskData.parameters.shape === -1 || this.props.invalid}
            onClick={this.submitRunNow}
          >
            Run Nowjson-schema-form-group-div
          </Button>
          <Button
            variant="primary"
            disabled={this.props.invalid}
            onClick={this.submitAddToQueue}
          >
            Add Diffraction Plan to Queue
          </Button>
        </ButtonToolbar>
      </Modal.Footer>
    );
  }

  showFooter() {
    const { isDiffractionPlan } = this.props.taskData;
    let foot = '';

    if (isDiffractionPlan) {
      foot = this.showDPFooter();
    } else {
      foot = this.showDCFooter();
    }
    return foot;
  }

  setConstraintsFromDefualts(schema) {
    const s = { ...schema }

    for (const key in this.props.initialValues) {
      if (s.properties[key]) {
        s.properties[key].default = this.props.initialValues[key]
      }
    }

    for (const key in this.props.taskData.Arraylimits) {
      if (s.properties[key]) {
        s.properties[key].exclusiveMinimum = this.props.taskData.limits[key][0]
        s.properties[key].exclusiveMaximum = this.props.taskData.limits[key][1]
      }
    }

    return s;
  }

  render() {
    function columnsObjectFieldTemplate({ properties, description }) {
      return (
        <div>
          <div className='row'>
            {properties.map(prop => {
              const {uiSchema} = prop.content.props
              const className = classNames('column', uiSchema['ui:column'] || 'col-6 json-schema-form-group-div')
              return <div key={prop.content.key} className={className}>
                {prop.content}
              </div>
            })}
          </div>
          {description}
        </div>
      )
    }

    const uiSchema = {
      "ui:order": [
        "num_images",
        "exp_time",
        "osc_range",
        "osc_start",
        "resolution",
        "transmission",
        "energy",
        "*",
      ],
      "ui:submitButtonOptions": {
        "norender": true,
      }
    };

    const schema = this.setConstraintsFromDefualts(
      this.props.schema.user_collection_parameters
    )

    return (
      <DraggableModal show={this.props.show} onHide={this.props.hide}>
        <Modal.Header closeButton>
          <Modal.Title>{this.props.taskData.name}</Modal.Title>
        </Modal.Header>
        <Modal.Body >
          <Form>
            <StaticField label="Path" data={this.props.path} />
            <StaticField label="Filename" data={this.props.filename} />
            <Row className='mb-2'>
              <Col xs={12} style={{ marginTop: '10px' }}>
                <InputField propName="subdir" label="Subdirectory" col1="2" col2="8" />
              </Col>
            </Row>
            <Row>
              <Col xs={12}>
                <InputField propName="prefix" label="Prefix" col1="2" col2="8" />
              </Col>
              {this.props.taskData.sampleID
                ? (
                  <Col xs={8}>
                    <InputField
                      propName="run_number"
                      disabled
                      label="Run number"
                      col1="4"
                      col2="3"
                    />
                  </Col>
                )
                : null}
            </Row>
          </Form>

          <FieldsHeader title="Acquisition" />
          <div className="json-schema-form-container">
            <JSForm
              liveValidate
              schema={schema}
              uiSchema={uiSchema}
              onChange={({ formData }) => {
                this.jsformData = formData;
              }}
              ObjectFieldTemplate={columnsObjectFieldTemplate}
            />
          </div>

        </Modal.Body>

        {this.props.taskData.state ? '' : this.showFooter()}

      </DraggableModal>
    );
  }
}

GenericTaskForm = reduxForm({
  form: 'GenericTaskForm',
  validate,
  warn
})(GenericTaskForm);

const selector = formValueSelector('GenericTaskForm');

GenericTaskForm = connect((state) => {
  const subdir = selector(state, 'subdir');
  let position = state.taskForm.pointID === '' ? 'PX' : state.taskForm.pointID;
  if (typeof position === 'object') {
    const vals = Object.values(position).sort();
    position = `[${vals}]`;
  }

  let fname = '';

  if (state.taskForm.sampleID) {
    fname = state.taskForm.taskData.parameters.fileName;
  } else {
    const prefix = selector(state, 'prefix');
    fname = `${prefix}_[RUN#]_[IMG#]`;
  }

  const { type } = state.taskForm.taskData;
  const {limits} = state.taskForm.defaultParameters[type];
  const {schema} = state.taskForm.defaultParameters[type];

  return {
    path: `${state.login.rootPath}/${subdir}`,
    filename: fname,
    acqParametersLimits: limits,
    schema,
    beamline: state.beamline,
    initialValues: {
      ...state.taskForm.taskData.parameters,
      type,
      beam_size: state.sampleview.currentAperture,
      resolution: (state.taskForm.sampleIds.constructor !== Array
        ? state.taskForm.taskData.parameters.resolution
        : state.beamline.hardwareObjects.resolution.value),
      energy: (state.taskForm.sampleIds.constructor !== Array
        ? state.taskForm.taskData.parameters.energy
        : state.beamline.hardwareObjects.energy.value),
      transmission: (state.taskForm.sampleIds.constructor !== Array
        ? state.taskForm.taskData.parameters.transmission
        : state.beamline.hardwareObjects.transmission.value),
      osc_start: (state.taskForm.sampleIds.constructor !== Array
        ? state.taskForm.taskData.parameters.osc_start
        : state.beamline.hardwareObjects["diffractometer.phi"].value)
    }
  };
})(GenericTaskForm);

export default GenericTaskForm;
