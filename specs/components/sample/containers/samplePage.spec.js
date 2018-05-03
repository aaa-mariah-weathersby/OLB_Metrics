import React from 'react';
import { mount } from 'enzyme';
import Chai from 'chai';
import Sinon from 'sinon';
import { mapStateToProps, SamplePage } from '../../../../src/components/sample/containers/samplePage';

Chai.should();

describe('Sample Page', () => {
  describe('Component', () => {
    let stubSampleAction;
    let subject;

    beforeEach(() => {
      stubSampleAction = Sinon.stub();
      subject = mount(<SamplePage sampleAction={stubSampleAction} />);
    });
    it('should render a span', () => {
      subject.find('#idSpan').length.should.equal(1);
    });
    it('should render a button', () => {
      subject.find('#idButton').length.should.equal(1);
    });
    describe('onClick', () => {
      it('should call sampleAction', () => {
        subject.find('#idButton').simulate('click');
        stubSampleAction.calledOnce.should.be.true;
      });
    });
  });

  describe('mapStateToProps', () => {
    it('should map sampleMessage', () => {
      const props = mapStateToProps({ samplePage: { sampleMessage: 'test', some: 'data', messageLoading: true } });
      props.should.eql({
        sampleMessage: 'test',
        sampleLoading: true,
      });
    });
  });
});
