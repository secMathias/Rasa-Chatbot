<template>
  <section class="client_section layout_padding">
    <div class="container">
      <div class="heading_container heading_center psudo_white_primary mb_45">
        <h2>
          What Our <span>Customers</span> Say
        </h2>
      </div>
      <div class="carousel-wrap">
        <div class="owl-carousel client_owl-carousel">
          <div class="item">
            <div class="box">
              <div class="img-box">
                <img src="@/assets/images/client1.jpg" alt="Client Image" class="box-img">
              </div>
              <div class="detail-box">
                <div class="client_id">
                  <div class="client_info">
                    <h6>
                      LusDen
                    </h6>
                    <p>
                      Satisfied Customer
                    </p>
                  </div>
                  <i class="fa fa-quote-left" aria-hidden="true"></i>
                </div>
                <p>
                  "Elite Financial Navigators provided me with exceptional service. Their expert management and secure investment strategies have significantly boosted my portfolio. I highly recommend their services to anyone looking to achieve financial success."
                </p>
              </div>
            </div>
          </div>
          <div class="item">
            <div class="box">
              <div class="img-box">
                <img src="@/assets/images/client2.jpg" alt="Client Image" class="box-img">
              </div>
              <div class="detail-box">
                <div class="client_id">
                  <div class="client_info">
                    <h6>
                      Zen Court
                    </h6>
                    <p>
                      Loyal Customer
                    </p>
                  </div>
                  <i class="fa fa-quote-left" aria-hidden="true"></i>
                </div>
                <p>
                  "The team at Elite Financial Navigators has been instrumental in guiding my investments. Their instant trading platform is top-notch, and their customer support is always responsive and helpful. I've seen great returns and feel confident in their expertise."
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ClientComponent'
}
</script>

<style scoped>
@import '../assets/css/bootstrap.css';
@import '../assets/css/font-awesome.min.css';
@import '../assets/css/style.css';
@import '../assets/css/responsive.css';
</style>
