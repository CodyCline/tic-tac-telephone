import { shallowMount ***REMOVED*** from '@vue/test-utils';
import HelloWorld from '@/components/HelloWorld.vue';

describe('HelloWorld.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message';
    const wrapper = shallowMount(HelloWorld, {
      propsData: { msg ***REMOVED***,
    ***REMOVED***;
    expect(wrapper.text()).toMatch(msg);
  ***REMOVED***;
***REMOVED***;
