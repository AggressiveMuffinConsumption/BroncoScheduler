import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import History from '@/components/History.vue'

describe('History.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message'
    const wrapper = shallowMount(History, {
      props: { msg }
    })
    expect(wrapper.text()).to.include(msg)
  })
})
