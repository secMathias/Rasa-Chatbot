<template>
  <section class="about_section layout_padding">
    <div class="container">
      <div class="heading_container heading_center">
        <h2>About <span>Us</span></h2>
        <p>Experience Expert Guidance and Cutting-Edge Technology for Your Financial Success</p>
      </div>
      <div class="row">
        <div class="col-md-6">
          <div class="img-box">
            <img src="@/assets/images/about-img.png" alt="">
          </div>
        </div>
        <div class="col-md-6">
          <div class="detail-box">
            <h3>We Are Elite</h3>
            <p>There are numerous brokers in the market, but few offer the combination of expertise, technology, and personalized service that we do. Our team of seasoned professionals is dedicated to providing you with the best investment opportunities, ensuring that you receive tailored advice and strategies that align with your financial goals. We understand that every client is unique, and we pride ourselves on delivering bespoke solutions.</p>
            <p>Our platform is built on cutting-edge technology, ensuring seamless and efficient trading experiences. We offer real-time data, advanced analytics, and robust risk management tools, all designed to help you make informed decisions and protect your investments. Transparency is at the heart of our operations, with competitive pricing and no hidden fees.</p>
            <router-link v-if="!isAboutPage" class="nav-link" to="/about">Read More</router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'AboutComponent',
  computed: {
    isAboutPage() {
      return this.$route.path === '/about';
    }
  }
}
</script>

<style scoped>
/* Add relevant styles if needed */
</style>
