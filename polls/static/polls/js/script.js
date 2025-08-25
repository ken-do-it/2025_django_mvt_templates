
// const good_job = document.getElementById('good_btn')

// good_job.addEventListener('click', (e)=>(console.log('good job')) )


document.addEventListener('DOMContentLoaded', () => {
  const good_job = document.getElementById('good_btn');
  if (good_job) {
    good_job.addEventListener('click', (e) => {
      console.log('good job');
    });
  }
});
